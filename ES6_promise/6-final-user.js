/*eslint-disable*/
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default (firstName, lastName, fileName) => Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
  .then((results) => results.map((promise) => ({
    status: promise.status,
    value: promise.status === 'fulfilled' ? promise.value : `${promise.reason.name}: ${promise.reason.message}`,
  })));
