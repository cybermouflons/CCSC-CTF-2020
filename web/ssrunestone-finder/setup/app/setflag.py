import redis, sys

if __name__ == "__main__":
    conn = redis.Redis(host='redis', port=6379)
    if len(sys.argv) < 2:
        raise Exception("[-] Flag not found in parameters. Please provide a flag in an .env file")
    conn.set("FLAG", sys.argv[1])
    print('[+] FLAG SET!')
