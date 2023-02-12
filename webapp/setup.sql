CREATE TABLE IF NOT EXISTS `books_reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_name` varchar(50) NOT NULL,
  `book_review` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- generate mock data for table `books_reviews`
INSERT INTO `books_reviews` (`id`, `book_name`, `book_review`) VALUES
(1, 'Test Book', 'Test Book'),
(2, 'Test Book', 'Test Book'),
(3, 'Test Book', 'Test Book'),
(4, 'Test Book', 'Test Book'),
(5, 'Test Book', 'Test Book'),
(6, 'Test Book', 'Test Book')