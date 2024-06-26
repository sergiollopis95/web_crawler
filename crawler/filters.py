class Filters:
    # Define a class named Filters to contain filtering methods.

    @staticmethod
    # Decorator defines a static method, meaning it can be called on the class itself, not on an instance.
    def filter_by_comments(entries):
        # Method to filter and sort entries by the number of comments.

        # Create a list of entries where the title has more than 5 words,
        # then sort this list by the number of comments (x[3]), in descending order (reverse=True)
        return sorted(
            [entry for entry in entries if len(entry[1].split()) > 5], 
            key=lambda x: x[3], 
            reverse=True
        )
    
    @staticmethod
    # Decorator defines another static method, meaning it can be called on the class itself, not on an instance.
    def filter_by_points(entries):
        # Method to filter and sort entries by the number of points

        # Create a list of entries where the title has 5 or fewer words,
        # then sort this list by the number of points (x[2]), in descending order (reverse=True)
        return sorted(
            [entry for entry in entries if len(entry[1].split()) <= 5], 
            key=lambda x: x[2], 
            reverse=True
        )
