class Wrapper:
    def wrap(self, line, wrap_width):
        if len(line) <= wrap_width:
            return line
        if line[wrap_width] == ' ':
            return line[0:wrap_width] + '\n' + self.wrap(line[wrap_width + 1:], wrap_width)
        space_pos = line.rfind(' ', 0, wrap_width)
        if space_pos < 0:
            return line[0:wrap_width] + '\n'+ self.wrap(line[wrap_width:], wrap_width)
        else:
            return line[0:space_pos] + '\n' + self.wrap(line[space_pos + 1:], wrap_width)
