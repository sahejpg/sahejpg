/**
 * @file my_string.c
 * @author SAHEJ PANAG
 * @collaborators NAMES OF PEOPLE THAT YOU COLLABORATED WITH HERE
 * @brief Your implementation of these famous 3 string.h library functions!
 *
 * NOTE: NO ARRAY NOTATION IS ALLOWED IN THIS FILE
 *
 * @date 2022-03-xx
 */

// DO NOT MODIFY THE INCLUDE(s) LIST
#include <stddef.h>
#include "hw7.h"

/**
 * @brief Calculate the length of a string
 *
 * @param s a constant C string
 * @return size_t the number of characters in the passed in string
 */
size_t my_strlen(const char *s)
{
  int len = 0;
  while (*s) {
    s++;
    len++;
  }

  return len;
}

/**
 * @brief Compare two strings
 *
 * @param s1 First string to be compared
 * @param s2 Second string to be compared
 * @param n First (at most) n bytes to be compared
 * @return int "less than, equal to, or greater than zero if s1 (or the first n
 * bytes thereof) is found, respectively, to be less than, to match, or be
 * greater than s2"
 */
int my_strncmp(const char *s1, const char *s2, size_t n)
{
  while (n != 0) {
    if (*s1 != *s2) {
      return ((*s1) - (*s2));
    }
    n--;
    s1++;
    s2++;
  }

  return 0;
}

/**
 * @brief Copy a string
 *
 * @param dest The destination buffer
 * @param src The source to copy from
 * @param n maximum number of bytes to copy
 * @return char* a pointer same as dest
 */
char *my_strncpy(char *dest, const char *src, size_t n)
{
  char *toReturn = dest;
  int strfake = my_strlen(src);
  if (my_strlen(src) < n) {
    int diff = n - strfake;
    int temp = strfake;
    while (temp != 0) {
      *dest = *src;
      dest++;
      src++;
      temp--;
    }
    while (diff != 0) {
      *dest = '\0';
      dest++;
      diff--;
    }
  } else {
    while (n != 0) {
      *dest = *src;
      dest++;
      src++;
      n--;
    }
  }
  return toReturn;
}
