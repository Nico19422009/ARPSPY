package main

import (
	"fmt"
	"net"
	"time"
)

func scanIP(ip string) {
	_, err := net.DialTimeout("tcp", ip+":80", 1*time.Second)
	if err == nil {
		fmt.Printf("%s is online\n", ip)
	}
}

func main() {
	for i := 1; i <= 254; i++ {
		ip := fmt.Sprintf("192.168.1.%d", i)
		go scanIP(ip)
	}

	// Wait for all scans to finish
	time.Sleep(10 * time.Second)
}
