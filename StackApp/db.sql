

CREATE TABLE public.answer
(
  answer_body character(1),
  date_posted date,
  question_id integer,
  posted_by character(50),
  answer_id integer NOT NULL,
  CONSTRAINT answer_key PRIMARY KEY (answer_id)
)
CREATE TABLE public.question
(
  question_id integer NOT NULL,
  body character(300),
  title character(100),
  date_posted date,
  posted_by character(50),
  CONSTRAINT question_pkey PRIMARY KEY (question_id)
)
CREATE TABLE public."User"
(
  user_id integer NOT NULL,
  names character(50),
  username character(50),
  email character(50),
  password character(30),
  CONSTRAINT "User_pkey" PRIMARY KEY (user_id)
)