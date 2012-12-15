<h2> students list</h2>>

<table>
  <tbody>
  %for student in students:
    <tr><td>${student.group_id}</td><td>${student.name}</td></tr>
  %endfor
  </tbody>
</table>
