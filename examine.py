from collections import defaultdict
try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest

_NONE_TYPE = type(None)
_EMPTY_TYPE = type('', (object,), {})
_MIXED_TYPE = type('<mixed-type>', (object,), {})


class AttrDict(dict):
    """A dict with keys accessible as attributes."""
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class Structure(object):
    """An object that reflects the structure of any python data structure.

    Any object may be passed to the constructor and a complete traverse of the
    structure occurs, making all the appropriate links so that the hierarchy
    may be examined. The str function will turn these objects into a simple
    representation of the structure with notations for lists and whether or
    not an attribute will be guaranteed for each particular branch.
    Also supported is adding different Structure objects, which will show only
    the structure common to both. Wherever the structure differs, it will
    be noted as a '<mixed-type>'
    """
    def __init__(self, value, key=None, parent=None):
        """Initialize a structure

        Takes the type of the value, and recursively creates sub-structures
        as children if the type is a list, tuple, or dict.
        """
        self.key = key
        self.parent = parent
        self.type_ = type(value)
        self.key_guaranteed = True
        self.val_guaranteed = True
        self.children = []

        if self.is_list:
            # Make a structure out of each item in the list
            list_items = [Structure(item, parent=self) for item in value]
            if list_items:
                # Add all structures together to get the common structure
                merged_structure = list_items[0]
                for item in list_items[1:]:
                    merged_structure += item
                # Set the only list child to the common structure
                merged_structure.parent = self
                self.children.append(merged_structure)
            else:
                self.children.append(Structure(_EMPTY_TYPE(), parent=self))
        elif self.is_tuple:
            # Make a structure out of each item in the tuple
            tuple_items = [Structure(item, parent=self) for item in value]
            if tuple_items:
                self.children = tuple_items
        elif self.is_dict:
            for key, val in value.items():
                self.children.append(Structure(val, key, self))
            self.children.sort(key=lambda child: child.key)

    def __add__(self, other):
        """Add structures to get a new structure that is common to both.

        The returned structure is a newly created structure that reflects the
        similarities and differences between the two structures added.
        """

        key_guaranteed = self.key_guaranteed and other.key_guaranteed
        val_guaranteed = self.val_guaranteed and other.val_guaranteed

        if self.type_ is other.type_:
            new = Structure(None, key=self.key)
            new.type_ = self.type_
            new.key_guaranteed = key_guaranteed
            new.val_guaranteed = val_guaranteed

            if self.is_list and other.is_list:
                listchild = self.children[0] + other.children[0]
                listchild.parent = new
                new.children.append(listchild)
                return new
            elif self.is_tuple and other.is_tuple:
                zipped = zip_longest(self.children, other.children)
                for schild, ochild in zipped:
                    if schild is None:
                        newchild = ochild.copy(new)
                        newchild.val_guaranteed = False
                        new.children.append(newchild)
                    elif ochild is None:
                        newchild = schild.copy(new)
                        newchild.val_guaranteed = False
                        new.children.append(newchild)
                    else:
                        newchild = schild + ochild
                        newchild.parent = new
                        new.children.append(newchild)
                return new
            elif self.is_dict and other.is_dict:
                keysdict = defaultdict(lambda: [None, None])
                for child in self.children:
                    keysdict[child.key][0] = child
                for child in other.children:
                    keysdict[child.key][1] = child
                for c1, c2 in keysdict.values():
                    if c1 is None:
                        newchild = c2.copy(new)
                        newchild.key_guaranteed = False
                    elif c2 is None:
                        newchild = c1.copy(new)
                        newchild.key_guaranteed = False
                    else:
                        newchild = c1 + c2
                        newchild.parent = new
                    new.children.append(newchild)
                new.children.sort(key=lambda child: child.key)
                return new
            else:
                return new
        else:
            if self.type_ is _EMPTY_TYPE:
                new = other.copy()
            elif other.type_ is _EMPTY_TYPE:
                new = self.copy()
            elif self.type_ is _NONE_TYPE:
                new = other.copy()
                new.key_guaranteed = key_guaranteed
                new.val_guaranteed = False
            elif other.type_ is _NONE_TYPE:
                new = self.copy()
                new.key_guaranteed = key_guaranteed
                new.val_guaranteed = False
            else:
                new = Structure(None, key=self.key)
                new.key_guaranteed = key_guaranteed
                new.val_guaranteed = val_guaranteed
                new.type_ = _MIXED_TYPE
            return new

    def __str__(self):
        """A structured representation of the underlying structure"""
        if self.parent:
            string = '{}{}{} - {}\n'.format(
                '  ' * (self.generation),
                '' if self.key_guaranteed else '*',
                self.key,
                self.type_string)
        else:
            string = '{}\n'.format(self.type_string)
        if self.children:
            if self.is_list:
                sub = self.children[0]
                while sub.is_list:
                    sub = sub.children[0]
                if sub.is_dict:
                    for child in sub.children:
                        string += str(child) + '\n'
            elif self.is_dict:
                for child in self.children:
                    string += str(child) + '\n'
        return string[:-1]

    def copy(self, parent=None):
        """Copies an existing structure and all of it's children"""
        new = Structure(None, parent=parent)
        new.key = self.key
        new.type_ = self.type_
        new.val_guaranteed = self.val_guaranteed
        new.key_guaranteed = self.key_guaranteed
        for child in self.children:
            new.children.append(child.copy(new))
        return new

    @property
    def generation(self):
        """Returns the number of ancestors that are dictionaries"""
        if not self.parent:
            return 0
        elif self.parent.is_dict:
            return 1 + self.parent.generation
        else:
            return self.parent.generation

    @property
    def type_string(self):
        """Returns a string representing the type of the structure"""
        if self.is_tuple:
            subtypes = [item.type_string for item in self.children]
            return '{}({})'.format(
                '' if self.val_guaranteed else '*',
                ', '.join(subtypes))
        elif self.is_list:
            return '{}[{}]'.format(
                '' if self.val_guaranteed else '*',
                self.children[0].type_string)
        else:
            return '{}{}'.format(
                '' if self.val_guaranteed else '*',
                self.type_.__name__)

    @property
    def is_list(self):
        return issubclass(self.type_, list)

    @property
    def is_tuple(self):
        return issubclass(self.type_, tuple)

    @property
    def is_dict(self):
        return issubclass(self.type_, dict)
