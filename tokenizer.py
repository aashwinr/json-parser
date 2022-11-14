class Tokenizer:
  def __init__(self, contents):
    self.content = contents
    self.pos = 0

  def next(self):
    return self.content[self.pos]

  def consume(self):
    next_val = self.next()
    self.pos += 1
    return next_val

  def consume_while(self, condition):
    consumed_string = ''
    while((not self.eof()) and condition(self.next())):
      consumed_string += self.consume()

  def consume_whitespace(self):
      self.consume_while(str.isspace)

  def consume_all_consecutive(self, char):
    def is_char(ch):
      return ch == char
    self.consume_while(is_char)

  def eof(self):
    return self.pos >= len(self.content)