#include <stdio.h>
#include <string.h>

int is_valid_flag(const char *flag) {
  char secret[] = {66,  84,  71, 87,  71, 81, 64, 124, 98,  123, 100,
                   125, 106, 75, 58,  64, 87, 35, 106, 106, 81,  38,
                   84,  92,  42, 114, 74, 82, 75, 112, 109, 98};
  for (int i = 0; i < 32; i++) {
    if ((flag[i] ^ i) != secret[i]) {
      return 0;
    }
  }
  return 1;
}

int main() {
  char input[33];
  printf("FLAG: ");
  fgets(input, 33, stdin);
  input[strcspn(input, "\n")] = 0;
  if (is_valid_flag(input)) {
    return 0;
  }
  return -1;
}
