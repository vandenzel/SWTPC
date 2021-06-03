#!/usr/bin/env python3

from textwrap import dedent


class Label:

    def __init__(self, address, label=None, comment=None, data=None, type=None):
        self.address = address
        self.label = label
        self.comment = comment
        self.data = data
        self.type = type

        self.update(label, comment, data, type)

    def update(self, label=None, comment=None, data=None, type=None):
        if label is not None:
            self.label = label
        if comment is not None:
            self.comment = comment
        if data is not None:
            self.data = data
        if type is not None:
            self.set_type(type)

    def set_type(self, type):
        if ':' in type:
            t, l = type.split(':')
        else:
            t = type
            l = 1

        try:
            l = int(l)
        except ValueError:
            l = 1
        self.type = t
        self.length = l

    def __str__(self):
        d = ''
        c = ''
        l = ''
        t = ''

        if self.label:
            if self.type == 'used':
                l = f'usedlabel {self.address:04x} {self.label}\n'
            else:
                l = f'label {self.address:04x} {self.label}\n'
        if self.data:
            d = f'data {self.address:04x}-{self.address + self.data-1:04x}\n'
        if self.comment:
            if ':' in self.comment:
                cc, lc = self.comment.split(':', maxsplit=2)
            else:
                cc, lc = self.comment, None
            if lc:
                for s in lc.split(';'):
                    c += f'lcomment {self.address:04x} {s}\n'
            if cc:
                c += f'comment {self.address:04x}\n'
                if cc == ' ':
                    pass
                else:
                    for s in cc.split(';'):
                        c += f'comment {self.address:04x} {s}\n'

        if self.type:
            if self.data:
                address = self.address
            else:
                address = self.address + 1

            if self.length > 1:
                upto = address + self.length - 1
                t = f'{self.type} {address:04x}-{upto:04x}\n'
            else:
                t = f'{self.type} {address:04x}\n'

        return d + c + l + t


class LabelList(dict):

    processor = None
    source = None

    def processor(self, p):
        self.processor = p

    def source(self, s):
        self.source = s

    def add(self, address, label=None, comment=None, data=None, type=None):
        if address in self:
            self[address].update(label, comment, data, type)
        else:
            self[address] = Label(address, label, comment, data, type)

    def __str__(self):

        pre = f"file    {self.source}\noption  {self.processor}\n\n"
        return pre + "\n".join([str(self[a]) for a in self])
