from modules.searchTheWeb import driver as searchTheWebDriver

def get_input_option(number_of_options):
    try:
        option = int(input())
        if option < 0 or option > number_of_options:
            raise Exception()
        
        return option - 1
    
    except:
        print("Invalid Input")
        return get_input_option(number_of_options)

def main():
    options = ["Search the web", "Prayer times", "Weather forecast", "Schedule a google calendar event", "Schedule a google meet", "Chat GPT"]
    print("Welcome, I'm Dwight!\nPlease select one of the following options:")
    for i in range(len(options)):
        print(f"{i + 1}: {options[i]}")

    op = get_input_option((len(options)))

    if options[op] == "Search the web":
        searchTheWebDriver()

if __name__ == "__main__":
    main()