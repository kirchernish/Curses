import datetime

def parse_date(date_str):
    formats = [
        "%A, %B %d, %Y",      # The Moscow Times
        "%A, %d.%m.%y",       # The Guardian
        "%A, %d %B %Y"        # Daily News
    ]
    
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def main():
    while True:
        date_input = input("Введите дату (или 'exit' для выхода): ")
        if date_input.lower() == 'exit':
            break
        
        parsed_date = parse_date(date_input)
        if parsed_date:
            print(parsed_date)
        else:
            print("Некорректный формат даты, попробуйте снова.")

if __name__ == "__main__":
    main()
