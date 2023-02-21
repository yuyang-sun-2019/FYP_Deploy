
use postgres://qwzfvmxbujfhbs:01f956c480a7f0365fffbb3ff26a29e1b765779557f84a03aeb06a3b6f9be08a@ec2-3-217-251-77.compute-1.amazonaws.com:5432/d1lqtpv46396rh 


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
