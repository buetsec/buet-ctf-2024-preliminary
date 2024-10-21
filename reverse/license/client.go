package main

import (
	"bufio"
	"crypto/sha256"
	"fmt"
	"net"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	server := "159.223.57.20:1740"

	fmt.Print("Name: ")
	name, _ := reader.ReadString('\n')
	name = name[:len(name)-1]

	fmt.Print("License key: ")
	key, _ := reader.ReadString('\n')
	key = key[:len(key)-1]

	license := fmt.Sprintf("%s$name$%s$key$%s", server, name, key)
	hash := sha256.Sum256([]byte(license))

	conn, err := net.Dial("tcp", server)
	if err != nil {
		fmt.Println("Error connecting to server: ", err)
		return
	}
	conn.Write([]byte(fmt.Sprintf("%x\n", hash)))

	response, _ := bufio.NewReader(conn).ReadBytes('\n')
	fmt.Println(string(response))
}
