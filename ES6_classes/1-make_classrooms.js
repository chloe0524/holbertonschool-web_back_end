/* eslint-disable */
import ClassRoom from './0-classroom.js';

export default () => {
  const arrAy = [19, 20, 34];
  const lesson = [];

  for (let size of arrAy) {
    lesson.push(new ClassRoom(size));
  }
  return lesson;
};
