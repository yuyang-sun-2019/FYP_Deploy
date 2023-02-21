use heroku_55f1bdb2075fced;

CREATE TABLE `user` (
 `email` varchar(50) NOT NULL,
 `hashed_password` varchar(256) ,
 `firstname` text NOT NULL,
 `lastname` text NOT NULL,
 PRIMARY KEY (`email`)
);

--
-- Dumping data for table `chat_id`
--

INSERT INTO `user` (`email`, `hashed_password`,`firstname`,`lastname`) VALUES
('x@x.com', "Qq1234567*",'john','john');
