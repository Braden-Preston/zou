"""empty message

Revision ID: 4e3738cdc34c
Revises: 6c597e842afa
Create Date: 2021-07-30 15:22:32.641313

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = '4e3738cdc34c'
down_revision = '6c597e842afa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_task_type_link', sa.Column('created_at', sa.DateTime(), nullable=True))

    op.add_column('project_task_type_link', sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True))
    op.execute('CREATE EXTENSION "uuid-ossp"')
    op.execute('UPDATE project_task_type_link SET id = uuid_generate_v4()')
    op.alter_column('project_task_type_link', 'id', nullable=False)

    op.add_column('project_task_type_link', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('project_task_type_link', sa.Column('priority', sa.Integer(), nullable=True))
    op.create_unique_constraint('project_tasktype_uc', 'project_task_type_link', ['project_id', 'task_type_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('project_tasktype_uc', 'project_task_type_link', type_='unique')
    op.drop_column('project_task_type_link', 'priority')
    op.drop_column('project_task_type_link', 'updated_at')
    op.drop_column('project_task_type_link', 'id')
    op.execute('DROP EXTENSION "uuid-ossp"')
    op.drop_column('project_task_type_link', 'created_at')
    # ### end Alembic commands ###
