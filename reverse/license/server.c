#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool validate_sha(const char *hash) {
  const char *should_start_with = "3ced3f96d70eecd4409f";
  if (strlen(hash) != 64) {
    return false;
  }
  for (int i = 0; i < 64; i++) {
    if (!((hash[i] >= 'a' && hash[i] <= 'f') ||
          (hash[i] >= '0' && hash[i] <= '9'))) {
      return false;
    }
  }
  return strncmp(hash, should_start_with, 20) == 0;
}

void setup() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
}

int main() {
  char hash[128];
  if (fgets(hash, 100, stdin) == NULL) {
    fprintf(stderr, "Failed to read input\n");
  }
  hash[strcspn(hash, "\n")] = 0;
  if (validate_sha(hash)) {
    const char *flag = getenv("FLAG");
    if (flag != NULL) {
      printf("Validation successfull!\nFlag: %s\n", flag);
    } else {
      printf("Flag not found.\nIf debugging in a local environment, make sure "
             "the FLAG environment variable is set.\nIf running against a "
             "remote server, contact the admin asap.");
    }
  } else {
    printf("The license is not registered or invalid.");
  }
  return 0;
}
