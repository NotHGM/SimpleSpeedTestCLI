import speedtest
import sys
import time

def list_top_servers(st, num_servers=5):
    closest_servers = st.get_closest_servers()
    top_servers = closest_servers[:num_servers]
    
    print("\nTop 5 servers in your area:")
    for i, server in enumerate(top_servers, 1):
        print(f"{i}. ID: {server['id']}, Server Name: {server['sponsor']}, Name: {server['name']}, Country: {server['country']}, City: {server['cc']}")

    return top_servers

def perform_test(st, server_id=None):
    if server_id:
        servers = st.get_servers()

        chosen_server = None
        for _, server_list in servers.items():
            for server in server_list:
                if server['id'] == server_id:
                    chosen_server = server
                    break
            if chosen_server:
                break

        if not chosen_server:
            print(f"Pick an ID closer to you: {server_id}")
            sys.exit(1)

        st.get_best_server(servers=[chosen_server])
    else:
        st.get_best_server()


    print("Performing download test...")
    start_time = time.time()
    download_speed = st.download()
    download_time = time.time() - start_time
    
    print("Performing upload test...")
    start_time = time.time()
    upload_speed = st.upload()
    upload_time = time.time() - start_time

    print("Performing ping test...")
    ping = st.results.ping

    return download_speed, upload_speed, ping, st.results.server, download_time, upload_time


def display_results(download, upload, ping, server, download_time, upload_time):
    print(f"\nResults:")
    print(f"Server: {server['name']} ({server['sponsor']})")
    print(f"Server ID: {server['id']}")
    print(f"Location: {server['country']}, {server['name']}")
    print(f"Download: {download / 1e6:.2f} Mbps (Time taken: {download_time:.2f} seconds)")
    print(f"Upload: {upload / 1e6:.2f} Mbps (Time taken: {upload_time:.2f} seconds)")
    print(f"Ping: {ping} ms")
    print("\nCreated by HGM")


def main():
    st = speedtest.Speedtest()
    
    print("Welcome to the Simple Speedtest CLI")
    print("1. Pick a specific server by ID")
    print("2. Automatic server selection")
    print("3. Choose from top 5 servers in your area")

    try:
        choice = input("Enter your choice (1/2/3): ")
        server_id = None
        if choice == '1':
            server_id = input("Enter the server ID you wish to test with: ")
        elif choice == '3':
            top_servers = list_top_servers(st)
            server_choice = int(input("Choose a server (1-5): "))
            server_id = top_servers[server_choice - 1]['id']
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        sys.exit(1)

    try:
        download, upload, ping, server, download_time, upload_time = perform_test(st, server_id)
        display_results(download, upload, ping, server, download_time, upload_time)
    except Exception as e:
        print("An error occurred during the test:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
