/*eslint-disable*/
export default (length, position, value) => {
  const view = new DataView(new ArrayBuffer(length)); position < 0 || position >= length ? (() => { throw new Error('Position outside range'); })() : view.setInt8(position, value);
  return view;
};
