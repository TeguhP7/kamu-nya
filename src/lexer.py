
import re

class Lexer(object):

    def __init__(self, kode_program):
        self.kode_program = kode_program

    def tokenize(self):

        tokens = []

        #Membuat daftar kata dari kode program
        kode_program = self.kode_program.split()

        source_index = 0

        #Loop
        while source_index < len(kode_program):

            kata = kode_program[source_index]

            if kata in ("var", "wew", "melu", "yes", "ashiap", "ok"):
                tokens.append(["VAR_DECLARATION", kata])

            elif re.match('[a-z]', kata) or re.match('[A-Z]', kata):
              if kata[len(kata) - 1] == ";":
                tokens.append(['IDENTIFIER', kata[0:len(kata) - 1]])
              else:
                tokens.append(['IDENTIFIER', kata])

            elif re.match('[0-9]', kata):
              if kata[len(kata) - 1] == ";":
                tokens.append(['INTEGER', kata[0:len(kata) - 1]])
              else:
                tokens.append(['INTEGER', kata])

            elif kata in "=/+=-+":
                tokens.append(['OPERATOR', kata])

            if kata[len(kata) - 1] == ";":
                tokens.append(['STATEMENT_END', ";"])

            source_index += 1

        print(tokens)

        return tokens