def ChkVowel(Ch):
    if Ch in ('a','e','i','o','u','A','E','I','O','U'):
        print("It is Vowel")
    else:
        print("It is not vowel")    


def main():
    Value = input("Enter the charater:\n")

    ChkVowel(Value)

if __name__ =="__main__":
    main()