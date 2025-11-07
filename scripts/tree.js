export function renderTree(data, parent, onFileClick) {
  data.forEach(item => {
    const container = document.createElement('div');
    container.style.marginLeft = '20px';

    if (item.type === 'folder') {
      const folderLabel = document.createElement('div');
      folderLabel.textContent = '📁 ' + item.name;
      folderLabel.classList.add('folder');

      const childrenContainer = document.createElement('div');
      childrenContainer.style.display = 'none';

      folderLabel.onclick = () => {
        childrenContainer.style.display =
          childrenContainer.style.display === 'none' ? 'block' : 'none';
      };

      container.appendChild(folderLabel);
      container.appendChild(childrenContainer);
      renderTree(item.children, childrenContainer, onFileClick);
    } else {
      const fileLabel = document.createElement('div');
      fileLabel.textContent = '📄 ' + item.name;
      fileLabel.classList.add('file');
      fileLabel.onclick = () => onFileClick(item.path);
      container.appendChild(fileLabel);
    }

    parent.appendChild(container);
  });
}
