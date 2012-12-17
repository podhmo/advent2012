<style type="text/css">
  ${layout.css}
</style>

<h2> students list(${layout.description})</h2>>

<table>
  <tbody>
  %for student in students:
    <tr><td>${student.group_id}</td><td>${student.name}</td></tr>
  %endfor
  </tbody>
</table>
