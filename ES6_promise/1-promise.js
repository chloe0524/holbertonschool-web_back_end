export default (success) => new Promise((resolve, reject) => {
  const status = 200;
  return success ? resolve(`status: ${status}, body: ${success}`) : reject(new Error('The fake API is not working currently'));
});
