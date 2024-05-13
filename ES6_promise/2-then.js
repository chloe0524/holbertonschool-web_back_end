export default function handleResponseFromAPI(promise) {
  return promise.then(() => {
    return { status: 200, body: 'Success' };
  })
    .then((response) => {
      console.log('Got a response from the API');
      return response || new Error('No response');
    })
    .catch(() => new Error());
}
