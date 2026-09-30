CREATE TABLE user_videos(
  id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE video(
  id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE user(
  id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_videos_id INTEGER,
  FOREIGN KEY (user_videos_id) REFERENCES user_videos(id)
);

CREATE TABLE videos(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_videos_id INTEGER,
  FOREIGN KEY (user_videos_id) REFERENCES user_videos(id)
);

CREATE TABLE watch_history( 
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_videos_id INTEGER,
  FOREIGN KEY (user_videos_id) REFERENCES user_videos(id)
);

create table analytics_videos(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  videos_id INTEGER,
  FOREIGN KEY (videos_id) REFERENCES videos(id)
);

CREATE TABLE likes_videos(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  videos_id INTEGER NOT NULL,
  FOREIGN KEY (videos_id) REFERENCES videos(id)
  FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE comments(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
  videos_id INTEGER, user_id INTEGER,
  content TEXT NOT NULL,
  FOREIGN KEY (videos_id) REFERENCES videos(id),
  FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE categories(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name varchar(100) NOT NULL UNIQUE,
  videos_id INTEGER,
  FOREIGN KEY (videos_id) REFERENCES videos(id)
);

CREATE TABLE playlist(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE department(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  moderator_id INTEGER,
  FOREIGN KEY (moderator_id) REFERENCES moderator(id)
);

CREATE TABLE moderators(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  video_id INTEGER,
  FOREIGN KEY (video_id) REFERENCES video(id)
);

CREATE TABLE user_notifications(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE subscriptions(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  users INTEGER,
  channel INTEGER,
  FOREIGN KEY (users) REFERENCES users(id),
  FOREIGN KEY (channel) REFERENCES channel(id)
);

CREATE TABLE channel(
  id INTEGER PRIMARY KEY AUTOINCREMENT
);
CREATE TABLE user_channel(
  id INTEGER PRIMARY KEY AUTOINCREMENT
);
CREATE TABLE tags(
  id INTEGER PRIMARY KEY AUTOINCREMENT
);
CREATE TABLE VIDEO_TAGS(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tags INTEGER,
  video INTEGER,
  FOREIGN KEY (tags) REFERENCES tags(id),
  FOREIGN KEY (video) REFERENCES video(id)
);
CREATE TABLE likes_comments(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  comments INTEGER,
  users INTEGER,
  FOREIGN KEY (comments) REFERENCES comments(id),
  FOREIGN KEY (users) REFERENCES users(id)
);
CREATE TABLE comment_mentions(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  comments INTEGER,
  FOREIGN KEY (comments) REFERENCES comments(id)
);
