# test_libft
Python script to test libft functions from 42 Paris

## To use it

You need a shared library instead of a static one.  
To do that you need to slightly modify your Makefile (or use another one):

- `libft.a` --> `libft.so`
- Add `-fPIC` flag when you compile (`-Wall -Werror -Wextra -fPIC`)
- `ar rc ...` --> `gcc -shared -o...`

Then put the python file at the root of the project (Where `libft.so` is)  
Then just run `python3 -m unittest`

## Active tests

**memset** :x:  
**bzero** :x:    
**memcpy** :x:   
**memccpy** :x:    
**memmove** :x:   
**memchr** :x:  
**memcmp** :x:   
**strlen** :heavy_check_mark:  
**isalpha** :heavy_check_mark:  
**isdigit** :heavy_check_mark:  
**isalnum** :heavy_check_mark:  
**isascii** :heavy_check_mark:  
**isprint** :heavy_check_mark:  
**toupper** :heavy_check_mark:  
**tolower** :heavy_check_mark:  
**strchr** :x:  
**strrchr** :x:  
**strncmp** :x:  
**strlcpy** :x:  
**strlcat** :x:  
**strnstr** :x:  
**atoi** :x:  
