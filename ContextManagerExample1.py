class MyCtx:
	def __init__(self, name, mode):
		self.name = name
		self.mode = mode
	def __enter__(self):
		print('Running enter')
		self.file = open(self.name, self.mode)
		return self
	def __exit__(self, exc_type, exc_value, exc_trace):
		print('Running exit')
		return False

class Tag:
    def __init__(self, tag):
        self.tag = tag
    
    def __enter__(self):
        print(f'<{self.tag}>', end='')
    
    def __exit__(self, exc_val, exc_type, exc_trace):
        print(f"</{self.tag}>", end="")
        return False

with Tag('p') as f:
    print('some', end='')
    with Tag('b'):
        print(' context', end='')
    print('end')

class Indent:
    def __init__(self, title, prefix='- ', indent=3):
        self.title = title
        self.prefix = prefix
        self.indent = indent
        self.current_indent = 0
        print(title)
    
    def __enter__(self):
        self.current_indent += self.indent
        return self
    
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.current_indent -= self.indent
        return False
    
    def print_item(self, arg):
        s = ' '* self.current_indent + self.prefix + str(arg)
        print(s)

with Indent('List1') as lm:
    lm.print_item('Item1')
    with lm:
        lm.print_item('SubItem1')
    lm.print_item('Item2')



