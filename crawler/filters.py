"""
This module defines the Filters class which contains methods to filter and sort
entries based on specific criteria such as the number of comments and points.
Classes:
--------
Filters:
    A class containing static methods to filter and sort entries.
Usage:
------
To use this module, you can call the static methods of the Filters class directly
without creating an instance of the class.
Example:
--------
    from filters import Filters
    filtered_by_comments = Filters.filter_by_comments(entries)
    filtered_by_points = Filters.filter_by_points(entries)
"""

class Filters:
    """
    A class to contain filtering methods for entries based on specific criteria.
    Methods:
    --------
    filter_by_comments(entries):
        Filters and sorts entries by the number of comments.
    
    filter_by_points(entries):
        Filters and sorts entries by the number of points.
    """

    @staticmethod
    def filter_by_comments(entries):
        """
        Filters and sorts entries by the number of comments.
        This method filters entries where the title has more than 5 words,
        and sorts them by the number of comments in descending order.
        Parameters:
        -----------
        entries : list of tuple
            A list of entries, where each entry is a tuple containing details of a news item.
            The structure of the tuple is assumed to be (number, title, points, comments).
        Returns:
        --------
        list of tuple
            A list of filtered and sorted entries by the number of comments.
        """
        return sorted(
            [entry for entry in entries if len(entry[1].split()) > 5], 
            key=lambda x: x[3], 
            reverse=True
        )

    @staticmethod
    def filter_by_points(entries):
        """
        Filters and sorts entries by the number of points.
        This method filters entries where the title has 5 or fewer words,
        and sorts them by the number of points in descending order.
        Parameters:
        -----------
        entries : list of tuple
            A list of entries, where each entry is a tuple containing details of a news item.
            The structure of the tuple is assumed to be (number, title, points, comments).
        Returns:
        --------
        list of tuple
            A list of filtered and sorted entries by the number of points.
        """
        return sorted(
            [entry for entry in entries if len(entry[1].split()) <= 5], 
            key=lambda x: x[2],
            reverse=True
        )