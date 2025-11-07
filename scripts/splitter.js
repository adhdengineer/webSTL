export function setupSplitter(splitterId, leftPaneId, min = 150, max = 600, onResize = null) {
  const splitter = document.getElementById(splitterId);
  const leftPane = document.getElementById(leftPaneId);

  let isDragging = false;

  splitter.addEventListener('mousedown', () => {
    isDragging = true;
    document.body.style.cursor = 'col-resize';
  });

  document.addEventListener('mouseup', () => {
    if (isDragging && onResize) {
        onResize();
    }
    isDragging = false;
    document.body.style.cursor = 'default';
  });

  document.addEventListener('mousemove', e => {
    if (!isDragging) return;
    const newWidth = Math.min(Math.max(e.clientX, min), max);
    leftPane.style.width = newWidth + 'px';
    if (onResize) {
        onResize();
    }    
  });
}
