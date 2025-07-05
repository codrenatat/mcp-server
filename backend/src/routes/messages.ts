import { Elysia, t } from 'elysia';
import type conversations from './conversations';

const messages = new Elysia({ prefix: '/messages' })
    // Obtenemos los mensajes de la base de datos
    
  .get( '/', async ({  }) => {
      const messages = [
        { 
            id: '1', 
            conversation_id: '1' 
        },
        { 
            id: '2', 
            conversation_id: '2'  
        }
      ];
      return messages;
    },
    {
      response: t.Array(
        t.Object({
          id: t.String(),
          conversation_id: t.String()
        })
      )
    }
  );

export default messages;