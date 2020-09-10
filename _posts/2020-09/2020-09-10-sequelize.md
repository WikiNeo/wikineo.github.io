---
title: "Sequelize notes"
published: true
tags: Node.js 
---

## Create migration files

```bash
cd migrations/
/path/to/node_modules/.bin/sequelize migration:create --name example
```

## Add and remove columns

```javascript
'use strict';

module.exports = {
  up: function (queryInterface, Sequelize) {
    /*
      Add altering commands here.
      Return a promise to correctly handle asynchronicity.

      Example:
      return queryInterface.createTable('users', { id: Sequelize.INTEGER });
    */
    return queryInterface.addColumn(
        'table_names',
        'column_name',
        {
            type: Sequelize.INTEGER,
            allowNull: true,
            comment: 'I am a comment?'

        }
    );
  },

  down: function (queryInterface, Sequelize) {
    /*
      Add reverting commands here.
      Return a promise to correctly handle asynchronicity.

      Example:
      return queryInterface.dropTable('users');
    */
     return queryInterface.removeColumn(
         'table_names',
         'column_name'
    );
  }
};
```

## Sequelize common types

```javascript
Sequelize.INTEGER
Sequelize.STRING
Sequelize.DATE
Sequelize.TEXT
```

## Running migrations

```bash
npx sequelize-cli db:migrate
```

## Undoing migrations

```bash
npx sequelize-cli db:migrate:undo
```

## Where

```javascript
tables.findAll({
    where: {
        name: {
            $ne: "haha"
        }
    }
})

tables.findOne({
    where: {
        name: {
            $eq: "haha"
        }
    }
})
```