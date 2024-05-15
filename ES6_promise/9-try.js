export default function guardfail(mathFunction) {
  const queue = [];
  queue.push(
    (() => {
      try {
        return mathFunction();
      } catch (err) {
        return `${err}`;
      }
    })(),
    'Guardrail was processed',
  );
  return queue;
}
