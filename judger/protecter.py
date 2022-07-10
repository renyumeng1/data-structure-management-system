class Protect:

    @staticmethod
    def check(lan,code)->str:
        unsafe_words_python = ["os", "subprocess"]
        if lan=="python3":
            checker=code.split("\r")
            for codes in checker:
                for word in codes.split():
                    if word in unsafe_words_python:
                        return "Unsafe"
