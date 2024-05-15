export default (numerator, denominator) => (denominator === 0 ? Promise.reject(new Error('cannot divide by 0')) : Promise.resolve(numerator / denominator));
