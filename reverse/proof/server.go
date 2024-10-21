package main

import (
	"bufio"
	"crypto/md5"
	"fmt"
	"os"
	"strings"
)

func validateHash(hash string) bool {
	shouldstartwith := "3b4913a4"
	return strings.HasPrefix(hash, shouldstartwith)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	name, _ := reader.ReadString('\n')
	name = strings.TrimSpace(name)
	key, _ := reader.ReadString('\n')
	key = strings.TrimSpace(key)

	license := fmt.Sprintf("name$%s$key$%s", name, key)
	hash := md5.Sum([]byte(license))
	hashString := fmt.Sprintf("%x", hash)

	if validateHash(hashString) {
		flag := os.Getenv("FLAG")
		if flag != "" {
			fmt.Println("Validation successful!")
			fmt.Printf("Flag: %s\n", flag)
		} else {
			fmt.Println("If you are testing in local environment, set the FLAG environment variable")
			fmt.Println("If you are running it against remote environment, contact admin asap")
		}
	} else {
		fmt.Println("The license is not registered or invalid.")
	}
}
