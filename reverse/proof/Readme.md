# proof

## Description

Prove that you can do it

[artifact](./chal.zip)

## Solution

Similar to license, The client is once again a facade for sending data to the server

The server now takes name, key as input and verifies it's 8 char md5 prefix

It sort of mimics proof of work. A 8 character hash collision can easily be found.
