DIAL_PAD = {
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
    "0": ["0"]
}


def phoneNumberMnemonics(phoneNumber):
    current_mnemonic = ['0'] * len(phoneNumber)
    mnemonics = []
    get_mnemonics(0, phoneNumber, mnemonics, current_mnemonic)
    return mnemonics


def get_mnemonics(index, phoneNumber, mnemonics, current_mnemonic):
    if index == len(phoneNumber):
        return mnemonics.append("".join((current_mnemonic)))
    else:
        digit = phoneNumber[index]
        possible_letters = DIAL_PAD[digit]
        for letter in possible_letters:
            current_mnemonic[index] = letter
            get_mnemonics(index + 1, phoneNumber, mnemonics, current_mnemonic)
