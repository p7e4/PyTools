#!/usr/bin/python3
# 子域存活检测

import sys
import requests
from multiprocessing.dummy import Pool as ThreadPool

def check(domain):
    if not (domain := domain.strip()): return
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36"
    }
    try:
        r = requests.get(f"http://{domain.strip()}", headers=headers,timeout=5,verify=False)
    except Exception as e:
        print(e)
    else:
        return domain


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 domain_check.py.py domain.txt result.txt")
    
    with open(sys.argv[1]) as f:
        data = f.readlines()

    pool = ThreadPool(processes=10)
    result = pool.map(check, data)
    pool.close()
    pool.join()

    with open(sys.argv[2], "w") as f:
        for i in list(set(result)):
            if i:
                f.write(i+"\r\n")


if __name__ == '__main__':
    main()

