import json


def authuser(email, code) -> bool:
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        
        with open('data.json', 'w') as f:
            data['users'][email] = {'code': code, 'verified': False}
            json.dump(data, f, indent=4)
            
        return True
                
    except FileNotFoundError as Error:
        print(str(Error))
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        return False
    except json.JSONDecodeError as Error:
        print(str(Error))
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        return False
    
def check_code(email):
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            
            print(data['users'][email]['code'])
    except FileNotFoundError as Error:
        print(str(Error))
        return False
    
    
check_code('adriii0104@hotmail.com')