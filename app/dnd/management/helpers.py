import random

def get_random_ua():
    random_ua = ''
    ua_file = "uafile.txt"
    try:
        with open(ua_file, "r") as f:
            lines = f.readlines()
        if len(lines) > 0:
            idx = random.randint(1,20)
            random_ua = lines[int(idx)]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_ua

#https://www.dndbeyond.com/spells?page=2
def get_referrer(num_or_name):
    if num_or_name == 1:
        return "https://www.dndbeyond.com/"
    if isinstance(num_or_name, int):
        return f"https://www.dndbeyond.com/spells?page={num_or_name - 1}"
    return f"https://www.dndbeyond.com/spells/{num_or_name}"
