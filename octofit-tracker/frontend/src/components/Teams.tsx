import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://glowing-lamp-qjjwp5x5r5wcxqpr-8000.app.github.dev/api/teams?format=api')
      .then(response => response.json())
      .then(data => setTeams(data));
  }, []);

  return (
    <div>
      <h2 className="text-primary">Teams</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Team Name</th>
          </tr>
        </thead>
        <tbody>
          {teams.map(team => (
            <tr key={team._id}>
              <td>{team.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Teams;
