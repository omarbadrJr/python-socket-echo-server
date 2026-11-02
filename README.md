# Lab 1: Echo Server

Group members: Omar Hany, ID : 2405729

## What it does

The client sends one message to the server. The first letter is the command:

- `A` sorts the remaining letters from Z to A.
- `C` sorts the remaining letters from A to Z.
- `D` changes the remaining text to uppercase.
- Any other first letter sends the message back unchanged.

## Run it

Open two terminals in this folder.

Terminal 1:

```sh
python3 echo_server.py
```

Terminal 2:

```sh
python3 echo_client.py
```

Type one message, for example `Cnetwork`.

## Simple explanation

1. The server waits on port `5050`.
2. The client connects and sends one message.
3. The server checks the first character and creates the reply.
4. The server sends the reply back.
5. The connection closes. The server waits for another client.

## Test examples

| Message | Reply |
| --- | --- |
| `Cnetwork` | `eknortw` |
| `Anetwork` | `wtronke` |
| `Dhello Network` | `HELLO NETWORK` |
| `Xhello` | `Xhello` |

## Screenshots and evidence

All evidence comes from the same run.

- `client_terminal.png` shows the four client tests, with the typed messages and replies.
- `server_terminal.png` shows the matching server output, including client addresses.
- `lab1_wireshark.png` shows the TCP data packets with the `tcp.len > 0` filter. The selected packet shows the payload `Cnetwork`.
- `wireshark_handshake.png` shows the full conversation with the `tcp.port == 5050` filter, including the TCP connection setup and teardown.
- `wireshark_follow_stream.png` shows one request and reply (Follow TCP Stream).
- `lab1.pcap` is the packet-capture file.
- `test_results.txt` has the text output of the tests and edge cases.

The capture has 8 data packets: 4 client requests and 4 server replies.
The client ports in the server log match the source ports in `lab1.pcap`.

## Edge cases

- A lowercase first letter such as `anetwork` is not a command, so the message is returned unchanged.
- Sorting uses character codes, so uppercase letters come before lowercase letters (`CnEtWork` gives `EWknort`).
- An empty message makes the client wait for a reply while the server waits for data. When the client is closed, the server crashes with `IndexError` because it reads the first character of an empty string. Empty input is not handled in this version.