export default (firstName) => Promise.reject(new Error(`${firstName} cannot be processed`));
