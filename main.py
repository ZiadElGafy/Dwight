def get_input_option(number_of_options):
    try:
        option = int(input())
        if option < 0 or option > number_of_options:
            raise Exception()
        
        return option
    except:
        print("Invalid Input")
        return get_input_option(number_of_options)

def main():
    options = ["Search the web", "Prayer times", "Weather forecast", "Schedule a google calendar event", "Schedule a google meet", "Chat GPT"]
    print("Welcome to Dwight!\nPlease select one of the following options:")
    for i in range(len(options)):
        print(f"{i + 1}: {options[i]}")

    print(get_input_option((len(options))))

if __name__ == "__main__":
    main()