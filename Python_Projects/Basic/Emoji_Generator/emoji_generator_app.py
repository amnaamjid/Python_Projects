#Project Name:Emoji Art Generator
#project No :2
#Caregory:Basic
#Day:2
#18-08-2023
#Programmer: Amna Amjid
#Programming language: Python



emoji_dict = {
    "happy": r"😄",
    "love": r"❤️",
    "sad": r"😢",
    "cool": r"😎",
    "laugh": r"😂",
    "angry": r"😡",
    "heart_eyes": r"😍"
}

def emoji_art_generator(sentence):
    words = sentence.lower().split()
    emoji_art =[]
    
    for word in words:
        if word in emoji_dict:
            emoji_art.append(emoji_dict[word])
        else:
            emoji_art.append(word)
            
    return " ".join(emoji_art)

def main():
    
    print("__Welcome to Emoji Art Generator__")
    print("f Program Instruction:\ Just write the emotion or emoji name the program will give you emoji based on your word or sentence")
    
    while True:
        user_input = input('Enter your word or "exist" for quiting:')
        if user_input == "exit":
            break
        
        emoji_art= emoji_art_generator(user_input)
        print( "Emoji Art:", emoji_art)
    
if __name__ == "__main__":
    main()