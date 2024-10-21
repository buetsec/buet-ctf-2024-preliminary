package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	server := "159.223.57.20:1310"

	fmt.Print("Name: ")
	name, _ := reader.ReadString('\n')
	name = name[:len(name)-1]

	fmt.Print("License key: ")
	key, _ := reader.ReadString('\n')
	key = key[:len(key)-1]

	conn, err := net.Dial("tcp", server)
	if err != nil {
		fmt.Println("Error connecting to server: ", err)
		return
	}
	conn.Write([]byte(fmt.Sprintf("%s\n%s\n", name, key)))

	response, _ := bufio.NewReader(conn).ReadBytes('}')
	fmt.Println(string(response))
}
