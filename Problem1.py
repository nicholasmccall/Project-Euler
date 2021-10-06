# Problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

###################### Solution Comments #############################
# My solution consists of looping over each value from 1 to the max multiple value
# and for each value, loop through the list of integers we want to find multiples for.
# If the current value we are on is a multiple of our integer (it is divisble by the int
# without a remainder) we break out of our sub-loop and add the integer to the running
# sum.
#
# Not in love with this solution as I'm sure there is a formula that can be applied
# here to calculate the solution in O(1).  I believe this solution is O(n^2) as the
# execution time scales with the maximum multiple and the number of integers in our
# list that was passed in.  There could be a faster solution if you knew the numbers
# were always going to be 3 and 5, but I assumed we would want the solution to work
# for any number of inputs.


def sum_multiples(integers, maximum_multiple) -> int:

    """
    For any value from 1 to maximum_multiple where the
    value is a multiple of one of the integers, sum the
    value.

    :param integers:
    :type integers: list of int
    :param maximum_multiple:
    :type maximum_multiple: int
    :return:
    """

    running_sum = 0

    for number in range(1, maximum_multiple):
        for divisor in integers:
            if number % divisor == 0:
                running_sum += number
                break

    return running_sum


if __name__ == '__main__':
    print(sum_multiples([3, 5], 1000))
